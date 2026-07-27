class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        ops = sorted(zip(position, speed), key=lambda v: v[0])
        ps = list(reversed(ops))
        fleets = 1
        for i, ((Fp, Fs), (Sp, Ss)) in enumerate(zip(islice(ps, 1, None), ps)):
            print(1, (Fp, Fs), (Sp, Ss))
            # ALGEBRA: Fp + FsT = Sp + SsT s.t. (Sp + SsT) < target
            # TODO: Miles needed and div by zero -> zero
            if (Ss - Fs) == 0:
                if Fp != Sp:
                    print("FLEET DONE", "div zero")
                    fleets += 1
                continue
            catchup_time_needed = (Fp - Sp) / (Ss - Fs)
            print(2, Fp + Fs * catchup_time_needed, target)
            # if the first car cannot catch up in time
            # or it would need to go back in time to catch up
            if catchup_time_needed < 0 or Fp + Fs * catchup_time_needed > target:
                print("FLEET DONE", Sp + Ss * catchup_time_needed)
                fleets += 1
            else:
                ps[i + 1] = (Sp, Ss)
        return fleets