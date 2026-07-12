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
