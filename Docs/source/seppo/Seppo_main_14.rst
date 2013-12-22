\tau_{t+1}=\s-248.0624 - 0.1242 Q_t - 0.3347 u_t
\tau_{t+1} &=& \tau(Q_t, u_t|\\u)
\sum_{t=0}^\\nfty \\eta^t \\eft[ A_0 Q_t - \\rac{A_1}{2}Q_t^2 - \\rac{d}{2} u_t^2 \right]
**Definition** Define a history :math:`Q^t=[Q_0, \\dots, Q_t]`. A history-dependent tax policy is a sequence of functions :math:`\\ igma_t\\_{t=0}^\\nfty` with time :math:`t` component :math:` igma_t` mapping :math:`Q^t` into a choice of :math:`\tau_{t+1}`.
**Definition** For any sequence :math:`\\c x=\\x_t\\_{t=0}^\\nfty`, :math:`\\ec x_1 \\quiv \\x_t\\_{t=1}^\\nfty` is called a *continuation* sequence or simply a *continuation*.
**Definition** Given a tax sequence :math:`\\au_{t+1}\\{t=0}^\\nfty`, a competitive equilibrium is a price sequence :math:`\\p_t\\_{t=0}^\\nfty` and an output sequence :math:`\\Q_t\\_{t=0}^\\nfty` that satisfy :eq:`ES_1`,  :eq:`ES_4`, and :eq:`ES_5`.
**Notation:** For any scalar :math:`x_t`, let :math:`\\c x=\\x_t\\_{t=0}^\\nfty`.
**Remark** A competitive equilibrium consists of a first period value :math:`u_0=\sQ_1-Q_0` and a continuation competitive equilibrium with initial condition :math:`Q_1`. A continuation of a competitive equilibrium is a competitive equilibrium.
**Remark** A continuation :math:`\\c \tau_1=\\\tau_{t+1}\\_{t=1}^\\nfty` of a tax policy :math:`\\ec \tau` influences :math:`u_0` via entirely through its impact on :math:`u_1`. A continuation competitive equilibrium can be indexed by a :math:`u_1` that satisfies .
**Remark** We could instead, perhaps with more accuracy, define a promised marginal value as :math:`\\ta (A_0 - A_1 Q_{t+1} ) - \\ta \tau_{t+1} + \rac{u_{t+1}}{\\ta}`, since this is the object to which the firm's first order condition instructs it to equate to the marginal cost :math:`d u_t` of :math:`u_t=q_{t+1} - q_t`. [3]_ But given :math:`(u_t, Q_t)`, the representative firm knows :math:`(Q_{t+1},\tau_{t+1})`, so it is adequate to take :math:`u_{t+1}` as the intermediate variable that summarizes how :math:`\\ec \tau_{t+1}` affects the firm's choice of :math:`u_t`.
.. math:: \tau_{t+1}=-F\\eft(\\egin{matrix} I & 0\\ -P_{22}^{-1}P_{21}&P_{22}^{-1}\\nd{matrix}\right)\\eft(\\egin{matrix} z_t \\\\ambda_{ut}\\nd{matrix}\right).
.. math:: \rac{\\rtial v}{\\rtial u_0}=0.
.. math:: F=\\eta(\\eta B'PB)^{-1}B'PA .
.. math:: P=\sR+A'PA-A'PB(B'PB)^{-1}B'PA
.. math:: Q_{t+1}=\sQ_t+u_t
.. math:: \\ft(\\gin{matrix} z_{t+1}\\lambda_{ut+1}\nd{matrix}\right)=\\eft(\\egin{matrix} I & 0 \\P_{21}&P_{22}\\nd{matrix}\right)(A-BF)\\eft(\\egin{matrix} I & 0\\ -P_{22}^{-1}P_{21}&P_{22}^{-1}\\nd{matrix}\right)\\eft(\\egin{matrix} z_t \\\\ambda_{ut}\\nd{matrix}\right)
.. math:: \\ft(\\gin{matrix}\\mbda_{zt}\\lambda_{ut}\nd{matrix}\right)=\\eft(\\egin{matrix} P_{11}&P_{12}\\P_{21}&P_{22}\\nd{matrix}\right)\\eft(\\egin{matrix} z_t \\u_t\\nd{matrix}\right) .
.. math:: u_t=-P_{22}^{-1}P_{21}z_t+P_{22}^{-1}\\ambda_{ut},
.. math:: u_{t+1}=-\\rac{A_0}d+\\rac{A_1}d Q_t+\\eft(\\rac{A_1}d+\\rac1\\eta\right)u_t+\\rac1d \tau_{t+1}.
.. math:: v(Q_t,\tau_t,u_t)=\\ax_{\tau_{t+1}} \\eft\\A_0 Q_t-\\rac {A_1}2 Q_t^2-\\rac d2 u_t^2+\\u\tau_tQ_t + \\eta v(Q_{t+1},\tau_{t+1},u_{t+1}) \right\\
.. math:: v(y_t)=\s-y_t'Py_t
.. math:: y_t=\\eft(\\egin{matrix} z_t\\ u_t\\nd{matrix}\right) = \\eft(\\egin{matrix} I & 0\\ -P_{22}^{-1}P_{21}&P_{22}^{-1}\\nd{matrix}\right)\\eft(\\egin{matrix} z_t \\\\ambda_{ut}\\nd{matrix}\right)
.. math:: y_{t+1}=Ay_t+B\tau_{t+1},
0=\\rac{\\artial}{\\artial u_0}\\eft(z_0'P_{11}z_0+z_0'P_{12}u_0+u_0'P_{21}z_0 +u_0' P_{22} u_0\right)=P_{12}'z_0+P_{21}u_0+2P_{22}u_0
Because this problem falls within the framework, we can proceed as follows. Letting :math:`\\mbda_t` be a vector of Lagrangian multipliers on the transition laws summarized in equation , it follows that :math:`\\mbda_t=\sP y_t`, where :math:`P` solves the Riccati equation
Define the selector vectors :math:`e_\tau=\\eft[\\egin{matrix} 0 & 0 & 1 & 0 \\nd{matrix}\right]'` and :math:`e_Q = \\eft[\\egin{matrix} 0 & 1 & 0 & 0 \\nd{matrix} \right]'`. Then express :math:`\tau_t = e_\tau' y_t` and :math:`Q_t = e_Q' y_t`. Evidently, tax revenues :math:`Q_t \tau_t = y_t' e_Q e_\tau' y_t = y_t' S y_t` where :math:`S \\quiv e_Q e_\tau'`. We want to compute
Equations :eq:`ES_1`,  :eq:`ES_4`, and :eq:`ES_5` summarize competitive equilibrium sequences for :math:`(\\c p, \\c Q, \\c u)` as functions of the path :math:`\\au_{t+1}\\{t=0}^\\nfty` for the flat rate distorting tax :math:`\tau`.
F=\\eta(\\eta B'PB)^{-1}B'PA = (B'PB)^{-1}B'PA .
G_t=\\eta \tau_{t+1} Q_{t+1} + \\eta G_{t+1}, \\uad t \\eq 0
G_{t+1} &=&\\eta^{-1} G_t -  \tau_{t+1} Q_{t+1}
Guess a solution that takes the form :math:`T_t=y_t' \\mega y_t ` then find an :math:`\\mega` that satisfies
It is important not to set :math:`q_t=\sQ_t` prematurely. To make the
J_t=A_0 Q_{t} & - &\\rac{A_1}{2} Q_{t}^2 - \\rac{d}{2} u_{t}^2   + \\eta J_{t+1} (\\at \tau_{t+1}, \\at G_{t+1}) \\
J_{t+1}(\tau_{t+1}, G_{t+1}) &=& \nu(Q_t, u_t, G_{t+1}, J_t, \tau_{t+1} )
Let :math:`u_t=\sq_{t+1} - q_t` be the firm's 'control' variable at time :math:`t`. First-order conditions for the firm's problem are
Notice how the Ramsey plan calls for a high tax at :math:`t=1` followed by a perpetual stream of lower taxes. Taxing heavily at first, less later sets up a time-inconsistency problem that we'll characterize formally after first discussing how to compute :math:`\\u`.
Of course, the representative firm sets :math:`u_t` in light of its expectations of how the government will ultimately choose to set future taxes. A credible tax plan :math:`\\au_{s+1}\\{s=t}^\\nfty` is one that is anticipated by the representative firm and also one that the government chooses to confirm.
P=\\eft(\\egin{matrix} P_{11}&P_{12}\\ P_{21}&P_{22}\\nd{matrix}\right)
Q_{t+1}=\sQ_t + u_t .
Q_{t+1} &=\s & Q_t + u_t
R=\\eft(\\egin{matrix} 0 & -\\rac {A_0}2 & 0 & 0 \\-\\rac{A_0}2 & \\rac{A_1}2 & \\rac {-\\u}{2}&0\\ 0 & \\rac{-\\u}{2}&0 & 0 \\ 0 & 0 & 0&\\rac d2\\nd{matrix}\right),
Ramsey plan and Ramsey outcome. From upper left to right, first panel: :math:`Q_t`; second panel, :math:`\tau_t`, third panel :math:`u_t=\sQ_{t+1} - Q_t`.
Recall that the Ramsey planner chooses :math:`\\_t\\{t=0}^\\nfty, \\\tau_t\\_{t=1}^\\nfty` to maximize
T_0=\sG_0
The matrix :math:`F` and therefore the matrix :math:`A_F=A-BF` depend on :math:`\\u`. To find a :math:`\\u` that guarantees that
The planner chooses :math:`\\_t\\{t=0}^\\nfty, \\\tau_t\\_{t=1}^\\nfty` to maximize :eq:`ES_Lagrange0` subject to :eq:`ES_4`, :eq:`ES_5`, and :eq:`ES_6`. To formulate this problem as a Lagrangian, attach a Lagrange multiplier :math:`\\u` to the budget constraint :eq:`ES_6`. Then the planner chooses :math:`\\u_t\\_{t=0}^\\nfty, \\\tau_t\\_{t=1}^\\nfty` to maximize and the Lagrange multiplier :math:`\\u` to minimize
The representative firm has given initial condition :math:`q_0`, endures quadratic adjustment costs :math:`\rac{d}{2} (q_{t+1} - q_t)^2`, and pays a flat rate tax :math:`\tau_t` per unit of output. The firm faces what it regards as exogenous sequences :math:`\\_t, \tau_t\\{t=0}^\\nfty` and chooses :math:`\\q_{t+1}\\_{t=0}^\\nfty` to maximize
To bring out the time inconsistency of the Ramsey plan, in figure :ref:`fig:ES_taudiff` we compare the time :math:`t` values of :math:`\tau_{t+1}` under the original Ramsey plan with the value :math:`\\eck \tau_{t+1}` associated with a new Ramsey plan begun at time :math:`t` with initial conditions :math:`(Q_t, G_t)` generated by following the *original* Ramsey plan, where again :math:`G_t=\\eta^{-t}(G_0- um_{s=1}^t\\eta^s\tau_sQ_s)`. Associated with the new Ramsey plan at :math:`t` is a value of the Lagrange multiplier on the continuation government budget constraint. In figure :ref:`fig:ES_udiff`, we compare the time :math:`t` outcome for :math:`u_t` under the original Ramsey plan with the time :math:`t` value of this new Ramsey problem starting from :math:`(Q_t, G_t)`. To compute :math:`u_t` under the new Ramsey plan, we use the following version of formula :
To compute a competitive equilibrium, it is appropriate to take , eliminate :math:`p_t` in favor of :math:`Q_t` by using , and then set :math:`q_t=\sQ_t`, thereby making the representative firm representative. [2]_ We arrive at
We computed the Ramsey plan for the following parameter values: :math:`[A_0, A_1, d, \beta, Q_0]=[100, .05, .2, .95, 100]`. Figure :ref:`fig:ES_plot_1` reports the Ramsey plan for :math:`\tau` and the Ramsey outcome for :math:`(Q_t,u_t)` for :math:`t=0, \\dots, 20`. [4]_ The optimal decision rule is [5]_
\\A=\\eft(\\egin{matrix}1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 1\\ 0 & 0 & 0 & 0 \\-\\rac{A_0}d & \\rac{A_1}d & 0 & \\rac{A_1}d+\\rac1\\eta\\nd{matrix}\right)\text{,  and  }B =\\eft(\\egin{matrix} 0 \\0 \\ 1 \\\\rac1d\\nd{matrix}\right).
\\eck{u_t}=- P_{22}^{-1} (\\heck\\u_{t}) P_{21}(\\heck\\u_t) z_t
\\ega=\\eta A_F' S A_F + \\eta A_F' \\mega A_F
\\ft(\\gin{matrix} z_0 \\ambda_{u0}\nd{matrix}\right)=\\eft(\\egin{matrix} 1\\ Q_0 \\\tau_0 \\0\\nd{matrix}\right).
\\ft(\\gin{matrix} z_0\\u_0\nd{matrix}\right)=\\eft(\\egin{matrix} z_0\\ -P_{22}^{-1}P_{21}z_0\\nd{matrix}\right).
\\ft(\\gin{matrix} z_t\\u_t\nd{matrix}\right)=\\eft(\\egin{matrix} I & 0\\ -P_{22}^{-1}P_{21}&P_{22}^{-1}\\nd{matrix}\right)\\eft(\\egin{matrix} z_t \\\\ambda_{ut}\\nd{matrix}\right)
\\ft(\\gin{matrix} z_{t+1}\\lambda_{ut+1}\nd{matrix}\right)=\\eft(\\egin{matrix} I & 0 \\P_{21}&P_{22}\\nd{matrix}\right)(A-BF)\\eft(\\egin{matrix} I & 0\\ -P_{22}^{-1}P_{21}&P_{22}^{-1}\\nd{matrix}\right)\\eft(\\egin{matrix} z_t \\\\ambda_{ut}\\nd{matrix}\right),
\\ft(\\gin{matrix} z_{t+1}\\u_{t+1}\nd{matrix}\right)=(A-BF)\\eft(\\egin{matrix} z_t\\ u_t\\nd{matrix}\right)
\\here :math:`z_t=\\eft(\\egin{matrix} 1 \\Q_t\\ \tau_t\\nd{matrix}\right)` are genuine state variables and :math:`u_t` is a jump variable. We include :math:`\tau_t` as a state variable for bookkeeping purposes: it helps to map the problem into a linear regulator problem with no cross products between states and controls. However, it will be a redundant state variable in the sense that the optimal tax :math:`\tau_{t+1}` will not depend on :math:`\tau_t`. The government chooses :math:`\tau_{t+1}` at time :math:`t` as a function of the time :math:`t` state. Thus, we can rewrite the Ramsey problem as
\\nd :math:`\tau_{t+1}=\s-F y_t`, where
\nt_0^Q[ A_0 - A_1 x]=A_0 Q - \\rac{A_1}{2} Q^2
\\t \tau_{t+1} &=& \tau(Q_t, u_t, G_t, J_t )
\\x_{\\_t\\\\au_{t+1}\\  um_{t=0}^\\nfty \\eta^t\\eft[A_0 Q_t-\\rac {A_1}2 Q_t^2-\\rac d2 u_t^2+\\u\tau_tQ_t\right]
\\x_{\\_t\\\\au_{t+1}\\ - um_{t=0}^\\nfty \\eta^t y_t' Ry_t
account the revenues already raised from :math:`s=1, \\dots, t` under
for all :math:`t \\q 0`, where :math:`Q_{t+1}=Q_t + u_t`. Under the timing protocol affiliated with the Ramsey plan, the planner is committed to the outcome of iterations on :eq:`ES_25`, :eq:`ES_26`, :eq:`ES_27`. In particular, when time :math:`t` comes, he is committed to the value of :math:`u_t` implied by the Ramsey plan and receives continuation value:math:`w(Q_t,u_t|\\u_0)`.
for all tax rates :math:`\tau_{t+1} \n {\\thbf R}` available to the government. Here :math:`\\t G_{t+1}=\\rac{G_t - \\at \tau_{t+1} Q_{t+1}}{\\eta}`. Inequality expresses that continuation values adjust to deviations in ways that discourage the government from deviating from the prescribed :math:`\\at \tau_{t+1}`.
p_t=A_0 - A_1 Q_t, \\uad A_0 >0, A_1 >0
subject to the terminal condition :math:`\\m_{t \rightarrow + \nfty} \\ta^t G_t=0`. Because the government is choosing sequentially, it is convenient to take :math:`G_t` as a state variable at :math:`t` and to regard the time :math:`t` government as choosing :math:`(\tau_{t+1}, G_{t+1})` subject to constraint :eq:`ES_govt_budget_sequential`.
u_0=\\psilon(Q_0, G_0, J_0),
u_t=\\rac{\\eta}{d} \\eft[ A_0 - A_1 Q_{t+1} \right] + \\eta u_{t+1} - \\rac{\\eta}{d} \tau_{t+1}
u_{t+1} &=& x(Q_t, u_t, G_t, J_t,{\tau_{t+1}} )
v(y_t)=\\ax_{\tau_{t+1}} \\eft\\ -y_t'Ry_t+\\eta v(y_{t+1}) \right\\ ,
w(Q_0,u_0|\\_0)=\sum_{t=0}^\\nfty \\eta^t \\eft[ A_0 Q_t - \\rac{A_1}{2}Q_t^2 - \\rac{d}{2} u_t^2 \right]
w(Q_t,u_t|\\_0)=A_0 Q_{t} - \\rac{A_1}{2} Q_{t}^2 - \\rac{d}{2} u_{t}^2  + \\eta w (Q_{t+1},u_{t+1}|\\u_0)
where :math:`A_F \\uiv A- BF`. Then using the initial state value :math:`\\mbda_{u,0}=0`, we obtain
where :math:`T_1=\sum_{t=2}^\\nfty \\eta^{t-1} Q_t \tau_t .` The present values :math:`T_0` and :math:`T_1` are connected by
where :math:`\\_t,u_t\\{t=0}^\\nfty` are evaluated under the Ramsey plan whose recursive representation is given by :eq:`ES_25`, :eq:`ES_26`, :eq:`ES_27` and where :math:`\\u_0` is the value of the Lagrange multiplier that assures budget balance, computed as described in section :ref:`sec:computing_mu`. Evidently, these continuation values satisfy the recursion
where :math:`\\au_t, Q_t\\{t=0}^\\nfty` is the original Ramsey outcome. [6]_ Then at time :math:`t \\eq 1`, take :math:`(Q_t, G_t)` inherited from the original Ramsey plan as initial conditions, and invite a brand new Ramsey planner to resolve to compute a new Ramsey plan, solving for a new :math:`u_t`, to be called , and for a new :math:`\\u`, to be called :math:`{\\heck \\u_t}`. The revised Lagrange multiplier  :math:`\\heck{\\u_t}`  is chosen so that, under the new Ramsey Plan, the government is able to raise enough continuation revenues :math:`G_t` given by :eq:`eqn:G_continuation`. Would this new Ramsey plan be a continuation of the original plan? The answer is no because along a Ramsey plan, for :math:`t \\eq 1`, in general it is true that
where :math:`z_t=\\eft(\\egin{matrix} 1\\r Q_t\\r \tau_t\\nd{matrix}\right)` are authentic state variables and :math:`u_t` is a variable whose time :math:`0` value is a 'jump' variable but whose values for dates :math:`t \\eq 1` will become state variables that encode history dependence in the Ramsey plan. Write a dynamic programming problem in the style of as
y_t=\\eft(\\egin{matrix}1\\r Q_t\\r \tau_t\\r u_t\\nd{matrix}\right) = \\eft(\\egin{matrix} z_t\\r u_t\\nd{matrix}\right),
y_{t+1}=\sA_F y_t ,

[General]
def_graphic_ext=
img_extIsRegExp=false
img_extensions=.eps .jpg .jpeg .png .pdf .ps .fig .gif
kileprversion=2
kileversion=2.1.3
lastDocument=
masterDocument=
name=Project
pkg_extIsRegExp=false
pkg_extensions=.cls .sty .bbx .cbx .lbx
src_extIsRegExp=false
src_extensions=.tex .ltx .latex .dtx .ins

[Tools]
MakeIndex=
QuickBuild=
