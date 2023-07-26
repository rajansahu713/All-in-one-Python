## Question
In a university, your attendance determines whether you will be
allowed to attend your graduation ceremony.
You are not allowed to miss classes for four or more consecutive days.
Your graduation ceremony is on the last day of the academic year,
which is the Nth day.

  Your task is to determine the following:

1. The number of ways to attend classes over N days.
2. The probability that you will miss your graduation ceremony.


## Explanation

Let’s call the day she/he absent as A. And the day she/he present as P

Then all possible attendance combinations for n=5 days will be –

'AAAAA', 'AAAAP', 'AAAPA', 'AAAPP', 'AAPAA', 'AAPAP', 'AAPPA', 'AAPPP', 'APAAA', 'APAAP', 'APAPA', 'APAPP', 'APPAA', 'APPAP', 'APPPA', 'APPPP', 'PAAAA', 'PAAAP', 'PAAPA', 'PAAPP', 'PAPAA', 'PAPAP', 'PAPPA', 'PAPPP', 'PPAAA', 'PPAAP', 'PPAPA', 'PPAPP', 'PPPAA', 'PPPAP', 'PPPPA', 'PPPPP' 

Now in combinations AAAAA, AAAAP and PAAAA, she/he absent for more than or equal to four consecutive days. Thus, we’ll reject these.

Required Combinations: 'AAAPA', 'AAAPP', 'AAPAA', 'AAPAP', 'AAPPA', 'AAPPP', 'APAAA', 'APAAP', 'APAPA', 'APAPP', 'APPAA', 'APPAP', 'APPPA', 'APPPP', 'PAAAP', 'PAAPA', 'PAAPP', 'PAPAA', 'PAPAP', 'PAPPA', 'PAPPP', 'PPAAA', 'PPAAP', 'PPAPA', 'PPAPP', 'PPPAA', 'PPPAP', 'PPPPA', 'PPPPP'-> 29 ways.

Now, in 14 combinations ('AAAPA', 'AAPAA', 'AAPPA', 'APAAA',  'APAPA','APPAA', 'APPPA', 'PAAPA', 'PAPAA', 'PAPPA', 'PPAAA', 'PPAPA', 'PPPAA' and 'PPPPA') from 29 possible combinations, she/he will not be able to attend the ceremony.

Thus, 

The number of ways to attend classes over 5 days is 29
The probability that you will miss your graduation ceremony is 14/29


### Pre-requisite
* Python should be install in your machine.

### To Run the program

* To begin, navigate to the directory containing the program file and open the terminal. Once the terminal is open, execute the command provided below.
```bash
python assignment.py
```
* In the terminal, you will be prompted to enter the number of days, as shown below.
```
Please enter the number of days: 5
```
* I am providing the number of days, which is 5.
* After pressing "Enter", the output below will be displayed in the terminal.
```
The number of ways to attend classes over 5 days is 29
The probability that you will miss your graduation ceremony is 14/29
``` 



