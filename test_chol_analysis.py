def test_HDL_analysis():
    from chol_analysis import HDL_analysis
    answer = HDL_analysis(100)
    expected = 'Normal'
    assert answer == expected
    

def test_HDL_analysis_2():
    from chol_analysis import HDL_analysis
    answer = HDL_analysis(40)
    expected = 'Borderline low'
    assert answer == expected
   