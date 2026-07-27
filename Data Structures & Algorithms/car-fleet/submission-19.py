class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        ps = sorted(zip(position, speed), reverse=True)
        fleets = 1
        Fp, Fs = ps[0]
        for Sp, Ss in islice(ps, 1, None):
            # ALGEBRA: Fp + FsT = Sp + SsT s.t. (Sp + SsT) < target
            if ((Ss - Fs) <= 0 and (Fp != Sp)) or Fp + Fs * (Fp - Sp) / (Ss - Fs) > target:
                fleets += 1
                Fp, Fs = Sp, Ss
        return fleets
