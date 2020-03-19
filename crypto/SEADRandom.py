import numpy as np


class SEADRandom:
    def __init__(self, seed1, seed2, seed3, seed4):
        self.state = [
            np.uint32(seed1),
            np.uint32(seed2),
            np.uint32(seed3),
            np.uint32(seed4)
        ]

    @classmethod
    def build(cls, seed1):
        seeds = [0, 0, 0, 0]
        current_seed = np.uint32(seed1)
        for i in range(4):
            seeds[i] = np.uint32(
                (np.uint32(0x6C078965) * (current_seed ^ (current_seed >> 30))) + i + 1
            )

            current_seed = seeds[i]

        return SEADRandom(seeds[0], seeds[1], seeds[2], seeds[3])

    def get_u32(self):
        v1 = np.uint32(self.state[0] ^ (self.state[0] << 11))
        self.state[0] = self.state[1]
        self.state[1] = self.state[2]
        self.state[2] = self.state[3]
        self.state[3] = v1 ^ (v1 >> 8) ^ self.state[3] ^ (self.state[3] >> 19)

        return self.state[3]

    def get_u64(self):
        v1 = np.uint32(self.state[0] ^ (self.state[0] << 11))
        v2 = self.state[1]
        v3 = np.uint32(v1 ^ (v1 >> 8) ^ self.state[3])
        self.state[0] = self.state[2]
        self.state[1] = self.state[3]
        self.state[2] = np.uint32(v3 ^ (self.state[3] >> 19))

        v4 = np.uint32(v2 ^ (v2 << 11))
        v5 = np.uint32(v4 >> 8)
        v6 = np.uint32(v3 >> 19)

        self.state[3] = v4 ^ v5 ^ self.state[2] ^ v6

        return np.uint64(self.state[2] << 32) | self.state[3]
