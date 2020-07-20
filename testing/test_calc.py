# 测试文件
import pytest

from calculator.calc import Calculator


class Test_calc:
    cal = Calculator()

    @pytest.mark.add
    @pytest.mark.parametrize('a, b, result', [(1, 1, 2),
                                              (2, 3, 5)
                                              ])
    def test_add(self, a, b, result):
        # cal = Calculator()
        assert result == self.cal.add(a, b)

    @pytest.mark.divi
    def test_divi(self):
        assert 1.1 == self.cal.divi(0.11, 0.10)
