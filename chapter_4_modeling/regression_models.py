'''
regression_models.py

Script that overviews implementation of various regression algorithms.
In this way, you can more easily get started on regression projects.

Goes through examples of:
1) linear regression
2) ridge regression
3) lasso regression
4) multi-task lasso
5) elastic net
6) multi-task elastic net
7) least-angle regression (LARS)
8) LARS lasso
9) orthogonal matching pursuit
10) bayesian ridge regression
11) automatic relevance determination
12) logistic regression
13) stochastic gradient descent
14) perceptron algorithms
15) pass-agressive algorithms
16) RANSAC
17) Theil-Sen
18) Huber Regression
19) Polynomial regression

For more information about regression, feel free to read the
Scikit-learn linear model documentation here:

http://scikit-learn.org/stable/modules/linear_model.html

'''
##################################################
##               IMPORT STATMENTS               ##
##################################################

from sklearn import linear_model
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import Perceptron
from sklearn.neural_network import MLPClassifier

##################################################
##################################################
##              MAIN CODE BASE                  ##
##################################################
##################################################
# generate some data
X = [[0., 0.], [1., 1.], [2., 2.], [3., 3.]]
Y = [0., 1., 2., 3.]

##################################################
##               linear regression              ##
##################################################
'''
LinearRegression fits a linear model with coefficients w = (w_1, ..., w_p)
to minimize the residual sum of squares between the observed responses
in the dataset, and the responses predicted by the linear approximation.

Example:
http://scikit-learn.org/stable/modules/linear_model.html
'''
ols = linear_model.LinearRegression()
ols.fit(X, y)
print(reg.coef_)

##################################################
##              Ridge regression                ##
##################################################
'''
Ridge regression addresses some of the problems of
Ordinary Least Squares by imposing a penalty on the
size of coefficients.

The ridge coefficients minimize a penalized residual sum of squares.

Example:
http://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Ridge.html#sklearn.linear_model.Ridge

'''
ridge = Ridge(fit_intercept=True, alpha=0.0, random_state=0, normalize=True)
reg.fit(X, Y)

##################################################
##                    LASSO                     ##
##################################################
'''
The Lasso is a linear model that estimates sparse coefficients.
It is useful in some contexts due to its tendency to prefer solutions
with fewer parameter values, effectively reducing the number of
variables upon which the given solution is dependent.

For this reason, the Lasso and its variants are fundamental
to the field of compressed sensing. Under certain conditions,
it can recover the exact set of non-zero weights
(see Compressive sensing: tomography reconstruction with L1 prior (Lasso)).

Example:
http://scikit-learn.org/stable/auto_examples/linear_model/plot_lasso_model_selection.html#sphx-glr-auto-examples-linear-model-plot-lasso-model-selection-py

'''
reg = linear_model.Lasso(alpha = 0.1)
reg.fit([[0, 0], [1, 1]], [0, 1])
reg.predict([[1, 1]])

##################################################
##              Multi-task LASSO                ##
##################################################
'''
The MultiTaskLasso is a linear model that estimates
sparse coefficients for multiple regression problems
jointly: y is a 2D array, of shape (n_samples, n_tasks).
The constraint is that the selected features are the same
for all the regression problems, also called tasks.

Example:
http://scikit-learn.org/stable/auto_examples/linear_model/plot_multi_task_lasso_support.html#sphx-glr-auto-examples-linear-model-plot-multi-task-lasso-support-py

'''
# Generate some 2D coefficients with sine waves with random frequency and phase
n_samples, n_features, n_tasks = 100, 30, 40
n_relevant_features = 5
coef = np.zeros((n_tasks, n_features))
times = np.linspace(0, 2 * np.pi, n_tasks)
for k in range(n_relevant_features):
    coef[:, k] = np.sin((1. + rng.randn(1)) * times + 3 * rng.randn(1))

X = rng.randn(n_samples, n_features)
Y = np.dot(X, coef.T) + rng.randn(n_samples, n_tasks)

coef_lasso_ = np.array([Lasso(alpha=0.5).fit(X, y).coef_ for y in Y.T])
coef_multi_task_lasso_ = MultiTaskLasso(alpha=1.).fit(X, Y).coef_

##################################################
##                  Elastic net                 ##
##################################################
'''
ElasticNet is a linear regression model trained with L1 and L2 prior as regularizer.
This combination allows for learning a sparse model where few of the weights are non-zero
like Lasso, while still maintaining the regularization properties of Ridge.

We control the convex combination of L1 and L2 using the l1_ratio parameter.

Example:
http://scikit-learn.org/stable/auto_examples/linear_model/plot_lasso_and_elasticnet.html#sphx-glr-auto-examples-linear-model-plot-lasso-and-elasticnet-py

'''
from sklearn.metrics import r2_score

# need training data 
enet = ElasticNet(alpha=alpha, l1_ratio=0.7)
y_pred_enet = enet.fit(X_train, y_train).predict(X_test)
r2_score_enet = r2_score(y_test, y_pred_enet)

##################################################
##            Multi-task elastic net            ##
##################################################
'''
The MultiTaskElasticNet is an elastic-net model that estimates sparse coefficients
for multiple regression problems jointly: Y is a 2D array, of shape (n_samples, n_tasks).

The constraint is that the selected features are the same for all the regression problems,
also called tasks.

Example:
http://scikit-learn.org/stable/modules/generated/sklearn.linear_model.MultiTaskElasticNet.html
'''
clf = linear_model.MultiTaskElasticNet(alpha=0.1)
clf.fit([[0,0], [1, 1], [2, 2]], [[0, 0], [1, 1], [2, 2]])
print(clf.coef_)
print(clf.intercept_)

##################################################
##          Least angle regression (LARS)       ##
##################################################
'''
The advantages of LARS are:

-> It is numerically efficient in contexts where p >> n (i.e., when the number of dimensions is significantly greater than the number of points)
-> It is computationally just as fast as forward selection and has the same order of complexity as an ordinary least squares.
-> It produces a full piecewise linear solution path, which is useful in cross-validation or similar attempts to tune the model.
-> If two variables are almost equally correlated with the response, then their coefficients should increase at approximately the same rate. The algorithm thus behaves as intuition would expect, and also is more stable.
-> It is easily modified to produce solutions for other estimators, like the Lasso.

The disadvantages of the LARS method include:

-> Because LARS is based upon an iterative refitting of the residuals,
-> it would appear to be especially sensitive to the effects of noise.

Example:
http://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Lars.html
'''
reg = linear_model.Lars(n_nonzero_coefs=1)
reg.fit([[-1, 1], [0, 0], [1, 1]], [-1.1111, 0, -1.1111])
print(reg.coef_)

##################################################
##                 LARS LASSO                   ##
##################################################
'''
LassoLars is a lasso model implemented using the LARS algorithm,
and unlike the implementation based on coordinate_descent,
this yields the exact solution, which is piecewise linear
as a function of the norm of its coefficients.

Example:
http://scikit-learn.org/stable/modules/linear_model.html#passive-aggressive-algorithms

'''
reg = linear_model.LassoLars(alpha=.1)
reg.fit([[0, 0], [1, 1]], [0, 1])
print(reg.coef_) 

##################################################
##      Orthogonal Matching Pursuit (OMP)       ##
##################################################
'''
OrthogonalMatchingPursuit and orthogonal_mp implements the OMP
algorithm for approximating the fit of a linear model with
constraints imposed on the number of non-zero coefficients (ie. the L 0 pseudo-norm).

Example:
http://scikit-learn.org/stable/auto_examples/linear_model/plot_omp.html#sphx-glr-auto-examples-linear-model-plot-omp-py
'''
n_components, n_features = 512, 100
n_nonzero_coefs=17
y, X, w = make_sparse_coded_signal(n_samples=1,
                                   n_components=n_components,
                                   n_features=n_features,
                                   n_nonzero_coefs=n_nonzero_coefs,
                                   random_state=0)

omp = OrthogonalMatchingPursuit(n_nonzero_coefs=n_nonzero_coefs)
omp.fit(X, y)
coef = omp.coef_

##################################################
##          Bayesian ridge regression           ##
##################################################
'''
The advantages of Bayesian Regression are:

-> It adapts to the data at hand.
-> It can be used to include regularization parameters in the estimation procedure.

The disadvantages of Bayesian regression include:

-> Inference of the model can be time consuming.

Example:
http://scikit-learn.org/stable/modules/generated/sklearn.linear_model.BayesianRidge.html
'''
clf = BayesianRidge()
clf.fit([[0,0], [1, 1], [2, 2]], [0, 1, 2])
clf.predict([[1, 1]])

##################################################
##      Automatic relevance determination       ## 
##################################################
'''
ARDRegression is very similar to Bayesian Ridge Regression,
but can lead to sparser weights w [1] [2]. ARDRegression poses
a different prior over w, by dropping the assumption of
the Gaussian being spherical.

Example:
http://scikit-learn.org/stable/auto_examples/linear_model/plot_ard.html#sphx-glr-auto-examples-linear-model-plot-ard-py
'''
n_samples, n_features = 100, 100
X = np.random.randn(n_samples, n_features)
relevant_features = np.random.randint(0, n_features, 10)

clf = ARDRegression(compute_score=True)
clf.fit(X, y)

##################################################
##              Logistic regression             ##
##################################################
'''
Logistic regression, despite its name, is a linear model
for classification rather than regression. Logistic regression
is also known in the literature as logit regression,
maximum-entropy classification (MaxEnt) or the log-linear classifier.

In this model, the probabilities describing the possible outcomes
of a single trial are modeled using a logistic function.

Example:
http://scikit-learn.org/stable/auto_examples/linear_model/plot_logistic_l1_l2_sparsity.html#sphx-glr-auto-examples-linear-model-plot-logistic-l1-l2-sparsity-py
'''
clf = linear_model.LogisticRegression(C=1.0, penalty='l1', tol=1e-6)
clf.fit(X, y)

##################################################
##      Stochastic gradient descent (SGD)       ##
##################################################
'''
Stochastic gradient descent is a simple yet very efficient
approach to fit linear models. It is particularly useful
when the number of samples (and the number of features) is very large.
The partial_fit method allows only/out-of-core learning.

The classes SGDClassifier and SGDRegressor provide functionality
to fit linear models for classification and regression using
different (convex) loss functions and different penalties.
E.g., with loss="log", SGDClassifier fits a logistic regression model,
while with loss="hinge" it fits a linear support vector machine (SVM).

Example:
http://scikit-learn.org/stable/modules/sgd.html#sgd
'''
n_samples, n_features = 10, 5
np.random.seed(0)
y = np.random.randn(n_samples)
X = np.random.randn(n_samples, n_features)
clf = linear_model.SGDRegressor()
clf.fit(X, y)

##################################################
##          Perceptron algorithms               ## 
##################################################
'''
Multi-layer Perceptron is sensitive to feature scaling,
so it is highly recommended to scale your data.
For example, scale each attribute on the input vector X to [0, 1] or [-1, +1],
or standardize it to have mean 0 and variance 1.

Note that you must apply the same scaling to the test
set for meaningful results. You can use StandardScaler for standardization.

change the solver to 'lbfgs'. The default'adam' is a SGD-like method,
hich is effective for large & messy data but pretty useless for this kind of smooth & small data.

Example:
http://scikit-learn.org/stable/modules/generated/sklearn.linear_model.PassiveAggressiveRegressor.html#sklearn.linear_model.PassiveAggressiveRegressor
'''

x = np.arange(0.0, 1, 0.01).reshape(-1, 1)
y = np.sin(2 * np.pi * x).ravel()
nn = MLPRegressor(
    hidden_layer_sizes=(10,),  activation='relu', solver='lbfgs', alpha=0.001, batch_size='auto',
    learning_rate='constant', learning_rate_init=0.01, power_t=0.5, max_iter=1000, shuffle=True,
    random_state=9, tol=0.0001, verbose=False, warm_start=False, momentum=0.9, nesterovs_momentum=True,
    early_stopping=False, validation_fraction=0.1, beta_1=0.9, beta_2=0.999, epsilon=1e-08)
n = nn.fit(x, y)

test_x = np.arange(0.0, 1, 0.05).reshape(-1, 1)
test_y = nn.predict(test_x)

##################################################
##          Passive-agressive algorithms        ##
##################################################
'''
The passive-aggressive algorithms are a family of algorithms
for large-scale learning. They are similar to the Perceptron
in that they do not require a learning rate. However,
contrary to the Perceptron, they include a regularization parameter C.

Example:
http://jmlr.csail.mit.edu/papers/volume7/crammer06a/crammer06a.pdf
'''
X, y = make_regression(n_features=4, random_state=0)
pa_regr = PassiveAggressiveRegressor(random_state=0)
pa_reg.fit(X,y)
pa_reg.coef_
pa.reg.intercept_
pa.reg.predict([0,0,0,0])

##################################################
##                   RANSAC                     ## 
##################################################
'''
When in doubt, use RANSAC

RANSAC (RANdom SAmple Consensus) fits a model from random subsets of
inliers from the complete data set.

RANSAC is a non-deterministic algorithm producing only a reasonable
result with a certain probability, which is dependent on the number
of iterations (see max_trials parameter). It is typically used for
linear and non-linear regression problems and is especially popular
in the fields of photogrammetric computer vision.

Example:
http://scikit-learn.org/stable/auto_examples/linear_model/plot_ransac.html#sphx-glr-auto-examples-linear-model-plot-ransac-py
'''
ransac = linear_model.RANSACRegressor()
ransac.fit(X, Y)
inlier_mask = ransac.inlier_mask_
outlier_mask = np.logical_not(inlier_mask)

##################################################
##              Theil-SEN                       ##
##################################################
'''
The TheilSenRegressor estimator uses a generalization of the median
in multiple dimensions. It is thus robust to multivariate outliers.

Note however that the robustness of the estimator decreases quickly
with the dimensionality of the problem. It looses its robustness
properties and becomes no better than an ordinary least squares
in high dimension.

Example:
http://scikit-learn.org/stable/auto_examples/linear_model/plot_theilsen.html#sphx-glr-auto-examples-linear-model-plot-theilsen-py

'''
theilsen=TheilSenRegressor(random_state=42)
theilsen.fit(X,y)

##################################################
##              Huber Regression                ##
##################################################
'''
The HuberRegressor is different to Ridge because it applies a linear loss
to samples that are classified as outliers. A sample is classified as an
inlier if the absolute error of that sample is lesser than a certain threshold.

It differs from TheilSenRegressor and RANSACRegressor because it does not
ignore the effect of the outliers but gives a lesser weight to them.

Example:
http://scikit-learn.org/stable/auto_examples/linear_model/plot_huber_vs_ridge.html#sphx-glr-auto-examples-linear-model-plot-huber-vs-ridge-py
'''

huber = HuberRegressor(fit_intercept=True, alpha=0.0,
                       max_iter=100, epsilon=epsilon)
huber.fit(X, y)
coef_ = huber.coef_ * x + huber.intercept_

##################################################
##              Polynomial Regression           ##
##################################################
'''
One common pattern within machine learning is to use linear models trained on
nonlinear functions of the data. This approach maintains the generally fast
performance of linear methods, while allowing them to fit a much wider range of data.

Example:
http://scikit-learn.org/stable/modules/linear_model.html#passive-aggressive-algorithms

'''

X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y = X[:, 0] ^ X[:, 1]
X = PolynomialFeatures(interaction_only=True).fit_transform(X).astype(int)
clf = Perceptron(fit_intercept=False, max_iter=10, tol=None,
                 shuffle=False).fit(X, y)
clf.predict(X)
clf.score(X, y)
