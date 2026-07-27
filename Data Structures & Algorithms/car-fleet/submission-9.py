class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        ps = sorted(zip(position, speed), reverse=True)
        fleets = 1
        for i, ((Fp, Fs), (Sp, Ss)) in enumerate(zip(islice(ps, 1, None), ps)):
            # ALGEBRA: Fp + FsT = Sp + SsT s.t. (Sp + SsT) < target
            if (Ss - Fs) == 0:
                if Fp != Sp:
                    fleets += 1
                continue
            catchup_time_needed = (Fp - Sp) / (Ss - Fs)
            # if the first car cannot catch up in time or it would need to go back in time to catch up
            if catchup_time_needed < 0 or Fp + Fs * catchup_time_needed > target:
                fleets += 1
            else:
                ps[i + 1] = (Sp, Ss)
        return fleets