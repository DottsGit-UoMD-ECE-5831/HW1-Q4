Q4) (Probability for Investigating Autonomous Vehicle Reliability) Read the following seminal
paper and answer the questions that will follow.
• Kalra, N. and Paddock, S.M., 2016. Driving to safety: How many miles of driving would it take
to demonstrate autonomous vehicle reliability? Transportation Research Part A: Policy and
Practice, 94, pp.182-193.

Q4a) How can binomial distributions be used for assessing the failure rates of autonomous
vehicles? Provide a detailed description/analysis in your own words.

A binomial distribution is a distribution with two outcomes that are mutually exclusive from each other, i.e. outcome A or Not A. So to assess the *failure* rate of autonomous vehicles (for which there is limited data), we can use 1 minus the *non-failure* rate of autonomous vehicles (for which there is much more data). The authors measure the failure rate of autonomous vehicles on a per-mile basis -- they estimate the confidence level in equation 1:

C = 1-R^n
where C = confidence level, R = 1-[failure rate per mile F], and n = number of failure-free miles.

This equation can be re-arranged to solve for n, the number of miles for no failures to achieve a given reliability rate:

n = ln(1-C) / ln(R)

Finally, this equation can also be re-arranged to solve for the failure rate F for a given confidence level C and number of miles n:

n		= ln(1-C) / ln(R)
n*ln(R)	= ln(1-C)
ln(R)	= ln(1-C)/n
R		= (1-C)^(-n)
1-F		= (1-C)^(-n)
F		= 1 - (1-C)^(-n)


Q4b) Write a python code to verify the example calculations in Section 2.2 of the paper.
Furthermore, write a Python code to reproduce the curve in Figure 1 of the paper.

See github.


Q4c) In your own words, describe the importance of the results provided in Kalra and Paddock’s
paper.

The results recreated here demonstrates the infeasibility of collecting comprehensive real-world safety statistical data by test-driving autonomous vehicles. The plot generated here is especially useful with the vertical reference lines that correspond to per-100-million-mile fatalities (1.09), reported injuries (77), estimated total injuries (103), reported crashes (190), and estimated total crashes (382) caused by human driving. The results estimate how many miles need to be test-driven to gather similarly statistically-balanced figures with various confidence levels. For example, at 95% confidence we would need to test-drive 275 million miles to get a value for the fatality rate that can be compared with that of human drivers, which is very impractical. This is due to the high confidence value of that estimate and a low fatality rate by human drivers. Meanwhile, at 50% confidence, we would only need closer to 200,000 test miles to compare an autonomous vehicle's estimated total crashes rate with that of human drivers, due to the low confidence percentage and since the human drivers estimated total crash rate is much higher than that of the fatality rate. This way of comparing failure rate therefore needs supporting studies to better capture the reliability of autonomous vehicles, which was performed in the following sections of the study.