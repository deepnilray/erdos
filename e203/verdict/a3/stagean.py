import numpy as np, sys
Es = [int(x) for x in sys.argv[1].split(',')]
B = [(5, 6), (6, 30), (30, 100), (100, 1000), (1000, 10000), (10000, 100000), (100000, 10**7)]
for E in Es:
    z = np.load(f'stages_E{E}.npz'); l = z['ells']; c = z['cost']; m1 = z['m1']; m2 = z['m2']; d = z['delta']; A = z['Acap']
    print(f"E={E}: total {c.sum():.6f}; stages {len(l)}; free (Acap<=delta) {(A<=d).sum()}")
    for lo, hi in B:
        k = (l >= lo) & (l < hi)
        print(f"   l in [{lo},{hi}): n_st={k.sum():5d} cost={c[k].sum():.4f}  m1={m1[k].sum():.4f}  m1raw={z['m1_raw'][k].sum():.4f} "
              f"m2={m2[k].sum():.5f} mean delta={d[k].mean() if k.any() else 0:.3f} free={(A[k]<=d[k]).mean() if k.any() else 0:.2f}")
    top = np.argsort(-c)[:12]
    print("   top stages:", [(int(l[i]), round(float(c[i]), 4), round(float(d[i]), 2), round(float(m1[i]), 3)) for i in top])
