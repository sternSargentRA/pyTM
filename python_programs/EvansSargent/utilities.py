import numpy as np
#function [f,p] = 
def olrp(beta,A,B,Q,R,W=None):
    '''
    %function [f,p] = olrp(beta,A,B,Q,R,W)
    
    %%OLRP can have arguments: (beta,A,B,Q,R) if there are no cross products
    
    %     (i.e. W=0).  Set beta=1, if there is no discounting.
    
    %
    
    %     OLRP calculates f of the feedback law:
    
    %               
    
    %		u = -fx
    
    %  
    
    %  that maximizes the function:
    
    %
    
    %          sum {beta^t [x'Qx + u'Ru +2x'Wu] }
    
    %  
    
    %  subject to 
    
    %		x[t+1] = Ax[t] + Bu[t] 
    
    %
    
    %  where x is the nx1 vector of states, u is the kx1 vector of controls,
    
    %  A is nxn, B is nxk, Q is nxn, R is kxk, W is nxk.
    
    %                
    
    %    Also returned is p, the steady-state solution to the associated 
    
    %  discrete matrix Riccati equation.
    
    %
    '''
    
    m=len(A)
    
    rb,cb=B.shape
    
    if not W:
        W= np.zeros((m,cb))
    
    p0=-.01*np.eye(m);
    
    dd=1;
    
    it=1;
    
    maxit=1000;
    
    #check tolerance; for greater accuracy set it to 1e-10
    
    while (dd>1e-6 and it<=maxit):
        #f0=   (R+beta*B'*p0*B)\(beta*B'*p0*A+W');
        f0 = np.linalg.solve(R+beta*B.T.dot(p0).dot(B),beta*B.T.dot(p0).dot(A)+W.T)        
        #p1=beta*A'*p0*A + Q -(beta*A'*p0*B+W)*f0;  
        p1 = beta*A.T.dot(p0).dot(A) + Q - (beta*A.T.dot(p0).dot(B)+W).dot(f0)
        #f1=   (R+beta*B'*p1*B)\(beta*B'*p1*A+W');  
        f1 = np.linalg.solve(R+beta*B.T.dot(p1).dot(B),beta*B.T.dot(p1).dot(A)+W.T)
        dd=np.max(np.max(np.abs(f1-f0)));        
        it=it+1;        
        p0=p1;
    
    f=f1;p=p0;
    
    if it>=maxit:
        print 'WARNING: Iteration limit of 1000 reached in OLRP'
    
    return f,p
