class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        ps = sorted(zip(position, speed), reverse=True)
        fleets = 1
        Fp, Fs = ps[0]
        for Sp, Ss in islice(ps, 1, None):
            # ALGEBRA: Fp + FsT = Sp + SsT s.t. (Sp + SsT) < target
            if (Ss - Fs) == 0:
                if Fp != Sp:
                    fleets += 1
                    Fp, Fs = Sp, Ss
            else:
                catchup_time_needed = (Fp - Sp) / (Ss - Fs)
                # if the first car cannot catch up in time or it would need to go back in time to catch up
                if catchup_time_needed < 0 or Fp + Fs * catchup_time_needed > target:
                    fleets += 1
                    Fp, Fs = Sp, Ss
            print(Fp, Fs)
        return fleets