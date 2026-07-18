from pathlib import Path

import pytest

from stress_test.data.non_native import load_icnale_written_essays, load_liang_toefl

LIANG_ROOT = Path("data/external/liang_toefl_src/Data_and_Results/Human_Data")


@pytest.mark.skipif(not LIANG_ROOT.exists(), reason="Liang TOEFL data not cloned locally")
def test_load_liang_toefl_marks_native_axis():
    records = list(load_liang_toefl(LIANG_ROOT))
    assert len(records) > 0
    assert all(r.label == 0 for r in records)  # all-human corpus
    non_native = [r for r in records if not r.meta["native"]]
    native = [r for r in records if r.meta["native"]]
    assert non_native and native
    assert {r.transform for r in non_native} == {"clean", "gpt4_polish"}


def test_apply_gold_edits_right_to_left_offsets():
    from stress_test.data.non_native import apply_gold_edits

    text = "I has a apple and I likes it."
    edits = [[0, [[2, 5, "have"], [6, 7, "an"], [20, 25, "like"], [10, 10, None]]]]
    assert apply_gold_edits(text, edits) == "I have an apple and I like it."
    assert apply_gold_edits(text, []) == text


def test_build_human_edit_records_preserves_doc_id_and_strips_edits():
    from stress_test.data import Record
    from stress_test.data.non_native import build_human_edit_records

    record = Record(
        text="She go to school.", label=0, doc_id="doc1", domain="wi_learner",
        generator="human", source_dataset="wi_locness", transform="clean",
        meta={"native": False, "cefr": "A2", "edits": [[0, [[4, 6, "goes"]]]]},
    )
    (edited,) = build_human_edit_records([record])
    assert edited.text == "She goes to school."
    assert edited.doc_id == "doc1"
    assert edited.transform == "human_edit"
    assert "edits" not in edited.meta and edited.meta["cefr"] == "A2"


def test_load_wi_locness_parses_bands(tmp_path):
    import json

    from stress_test.data.non_native import load_wi_locness

    (tmp_path / "A.train.json").write_text(
        json.dumps({"id": "1", "text": "Learner essay text here.", "cefr": "A2.i",
                    "userid": "u1", "edits": [[0, [[0, 7, "Student"]]]]}) + "\n",
        encoding="utf-8",
    )
    (tmp_path / "N.dev.json").write_text(
        json.dumps({"id": "2", "text": "Native essay text here.", "cefr": None,
                    "userid": "u2", "edits": []}) + "\n",
        encoding="utf-8",
    )
    records = list(load_wi_locness(tmp_path))
    by_domain = {r.domain: r for r in records}
    assert by_domain["wi_learner"].meta["native"] is False
    assert by_domain["wi_learner"].meta["cefr"] == "A2.i"
    assert by_domain["locness"].meta["native"] is True
    assert by_domain["locness"].meta["cefr"] == "N"


def test_load_icnale_raises_clear_error_when_missing(tmp_path):
    with pytest.raises(FileNotFoundError, match="unzip"):
        list(load_icnale_written_essays(tmp_path / "nonexistent"))


def test_load_icnale_parses_filename_convention(tmp_path):
    (tmp_path / "WE_CHN_PTJ0_001_B1_2.txt").write_text("Sample essay text here.", encoding="utf-8")
    (tmp_path / "WE_ENS_PTJ0_050_NS.txt").write_text("Native speaker essay.", encoding="utf-8")
    records = list(load_icnale_written_essays(tmp_path))
    assert len(records) == 2
    by_region = {r.meta["region"]: r for r in records}
    assert by_region["CHN"].meta["native"] is False
    assert by_region["ENS"].meta["native"] is True
    assert by_region["CHN"].meta["cefr"] == "B1_2"
