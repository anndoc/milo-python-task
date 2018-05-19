from main import main


class TestMain:
    def test_success(self):
        assert main('1/1/2000') == '2000-01-01'
        assert main('2000/1/1') == '2000-01-01'
        assert main('00/1/1') == '2000-01-01'
        assert main('1/01/00') == '2000-01-01'
        assert main('0/1/1') == '2000-01-01'
        assert main('1/0/1') == '2000-01-01'
        assert main('1/1/0') == '2000-01-01'
        assert main('2999/2/6') == '2999-02-06'
        assert main('1/2/6') == '2001-02-06'
        assert main('01/2/6') == '2001-02-06'
        assert main('2001/2/6') == '2001-02-06'
        assert main('2999/31/12') == '2999-12-31'

    def test_leap_year(self):
        assert main('2012/29/2') == '2012-02-29'
        assert main('29/2012/2') == '2012-02-29'
        assert main('29/2/2012') == '2012-02-29'

    def test_illegal_date(self):
        assert main('2011/29/2') == '"2011/29/2" is illegal'
        assert main('2011/2/29') == '"2011/2/29" is illegal'
        assert main('1999/2/20') == '"1999/2/20" is illegal'
        assert main('2000/13/20') == '"2000/13/20" is illegal'
        assert main('3000/12/20') == '"3000/12/20" is illegal'

    def test_wrong_date(self):
        assert main('29/2') == '"29/2" is illegal'
        assert main('29/2/20000') == '"29/2/20000" is illegal'
        assert main('') == '"" is illegal'
        assert main('test/1/1') == '"test/1/1" is illegal'
