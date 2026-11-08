from sympy import symbols, simplify, together, Rational, expand
m,u,t=symbols('m u t', positive=True)
n=m*u*t-m-u
w=(m*t-1)/4
X=u*t-1
lhs=4/n
rhs=1/(u*w)+1/(n*w*X)+1/(u*w*X)
print("Theorem A symbolic difference:", simplify(together(lhs-rhs)))
# planted-failure control: change X to u*t (wrong) must NOT simplify to 0
bad=1/(u*w)+1/(n*w*(u*t))+1/(u*w*(u*t))
print("control (wrong X) difference zero?", simplify(together(lhs-bad))==0)
# Proposition B algebra: (mt-1)(ut-1) = n t + 1
print("(mt-1)(ut-1)-(nt+1) =", expand((m*t-1)*(u*t-1)-(n*t+1)))
