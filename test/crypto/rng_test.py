from crypto.SEADRandom import SEADRandom

def test_32():
    rand = SEADRandom.build(0x123)

    assert rand.get_u32() == 2810884293
    assert rand.get_u32() == 2210740354
    assert rand.get_u32() == 3725763208
    assert rand.get_u32() == 3148902586
    assert rand.get_u32() == 1229910929

def test_64():
    rand = SEADRandom.build(0x123)

    assert rand.get_u64() == 12072656113485822082
    assert rand.get_u64() == 16002031134148948154
    assert rand.get_u64() == 5282427220871467794
    assert rand.get_u64() == 12153010893065923339
    assert rand.get_u64() == 12558587682029648749
