'''
given x, y points product a best fit straight line.
'''


# imports go here
import numpy as np
from sklearn.linear_model import LinearRegression


def main():
    ''' main entry point for the code '''
    run_the_numbers()
    return


def run_the_numbers():
    ''' the function doc string '''
    x, y = create_lists()
    slope, intercept = best_fit_line_numpy(x, y)
    print('numpy array method:')
    print(f'slope: {slope:.2f}, intercept: {intercept:.2f}')

    print('-------')

    slope, intercept = best_fit_line_regress(x, y)
    print('sklearn linear regression method:')
    print(f'slope: {slope:.2f}, intercept: {intercept:.2f}')    
    return


def best_fit_line_numpy(x:np.ndarray, y:np.ndarray)-> tuple[float, float]:
    ''' straight line using the numpy 
    
    args:
        x: the x ordinates
        y: the y ordinates

    return:
        tuple (slope, intercept)

    '''
    m = ( (x.dot(y) - y.sum()*x.sum()/x.size) /  
        (x.dot(x) - x.sum()**2/x.size) )

    b = (y.sum()/y.size) - m*(x.sum()/x.size)

    # print(f"Equation of best fit line:") 
    # print(f"y = {m:.2f}x + {b:.2f}")
    return m, b


def best_fit_line_regress(x:np.ndarray, y:np.ndarray)-> tuple[float, float]:
    ''' straight line using the sklearn LinearRegression model 
    
    args:
        x: the x ordinates
        y: the y ordinates

    return:
        tuple (slope, intercept)

    '''
    
    x = np.array(x).reshape((-1, 1))
    y = np.array(y)

    model = LinearRegression()
    model.fit(x, y)

    m = model.coef_ # slope
    b = model.intercept_ # intercept

    # print(f"Equation of best fit line:") 
    # print(f"y = {m[0]:.2f}x + {b:.2f}")    
    return m[0], b


def time_code():
    return

def create_lists():
    ''' make numpy.ndarray lists '''
    x = np.array([1, 2, 3, 4, 10]) 
    y = np.array([2, 4, 6, 8, 10])
    return x, y




# main guard idiom
if __name__=='__main__':
    main()
