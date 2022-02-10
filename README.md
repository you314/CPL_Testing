# Documentation of cpl testing tool
This tool will support the cpl development by ensuring the calculation 
of reliable outcomes for actuarial values (e.g. prospective reserves, net premium, accounting).

## Architecture

__Open:__ Illustrate how the testing tool interacts with the outcome of cpl and where this tool is located in the 
general software architecture. 

## Structure

The program is structured in packages, resembling the data flow.

1. __input:__ Builds the contract instance which is relevant for the calculation base classes. The input file will be a
test file, which can be used by cpl as well. 
2. __calculationbases:__ This package contains many subpackages which provide, biometrical values, costs, interests, 
flags and terms.
3. __calculationengine:__ Tariff logic used to calculate actuarial values. It needs to be decided if one engine per 
tariff class is needed. 
4. __output:__ This method is empty still, but it will be used to perform the comparison between cpl's and python's
output. Yielding a comparison file. 

The two remaining packages cannot be fit into the data flow.

- __helper:__ All modules that have no direct link to the actuarial calculations are stored here. Those are customized
csv readers, or the c_file reader (used to read the cpl output).
- __tests:__ All classes and functions in this tool should be covered by a unit tests. Those tests can be found here.

### input
Please find the current documentation of the external interface - ABS table / column mapping here:

e_Benefit_raw = json.dumps(data['contract']['TLSCHDETAIL']['new'][0]['SUMME']) \
e_BenefitSurvivRatio_raw = json.dumps(data['contract']['TPRODAUS']['new'][0]['SUMME'])\
e_Courtage_raw = 0 \
e_DefermentPeriod_raw = json.dumps(data['contract']['TPENSVEREINBG']['new'][0]['RENTENAUFDAUER']) \
e_PaymDuration_raw =  json.dumps(data['contract']['TLEBENSCHICHT']['new'][0]['PRZAHLDAUER']) \
e_PensionDynamic_raw = "unclear" \
e_PremPaymentFreq_raw = json.dumps(data['contract']['TVERTRAG']['new'][0]['ZAHLWEISE']) \
e_Tariff_raw = json.dumps(data['contract']['TLSCHDETAIL']['new'][0]['TARBEZEICHNUNG'])  \

e_benefitPeriod_raw = json.dumps(data['contract']['TLEBENSCHICHT']['new'][0]['LEISTUNGSDAUER']) \
e_guaranteePeriod_raw = json.dumps(data['contract']['TPENSVEREINBG']['new'][0]['REVERGARZEIT']) \
e_m_raw = 0 # Check if m is calculated by calcdate-begindate \
e_n_raw = json.dumps(data['contract']['TLEBENSCHICHT']['new'][0]['VERSDAUER']) \

e_AddSurcharge_IP1_raw = 0 # Maybe in TZUSKOSTEN \
e_AddSurcharge_IP2_raw = 0 \
e_BirthDate_IP1_raw = json.dumps(data['contract']['TNATPERS']['new'][0]['GEBURTSDATUM']) \
e_BirthDate_IP2_raw = 0 # Second insured personis probably second item of TNATPERS \
e_ea_IP1_raw = json.dumps(data['contract']['TVERSPERS']['new'][0]['EINTRALTER']) \
e_ea_IP2_raw = 0 # Second insured personis probably second item of TVERSPERS \
e_gender_IP1_raw = json.dumps(data['contract']['TNATPERS']['new'][0]['GESCHLECHT']) \
e_gender_IP2_raw = 0 # Second insured personis probably second item of TNATPERS \
e_HealthClass_IP1_raw = json.dumps(data['contract']['TVERSPERS']['new'][0]['ZUSCHLKLASSE']) \
e_HealthSurch_IP1_raw = 0 #-> Calc logiv in IL: /abs-rss-cpl/blob/main/ABS_MATHLIFE/src/math_life/vp/tlife_ip_surcharges.cpp \
e_numberOfInsPers_raw = 0 #-> Count arrays in ['TVERSPERS']? \
e_OccuClass_raw = 0 #-> Calc logiv in IL: /abs-rss-cpl/blob/main/ABS_MATHLIFE/src/math_life/vp/tlife_ip_surcharges.cpp \
e_OccuSurcha_IP1_raw = 0 #-> Calc logiv in IL: /abs-rss-cpl/blob/main/ABS_MATHLIFE/src/math_life/vp/tlife_ip_surcharges.cpp \
e_RiskGroup_IP1_raw = 0 #-> Calc logiv in IL: /abs-rss-cpl/blob/main/ABS_MATHLIFE/src/math_life/vp/tlife_ip_attributes.cpp \
e_RiskGroup_IP2_raw = 0 #-> Calc logiv in IL: /abs-rss-cpl/blob/main/ABS_MATHLIFE/src/math_life/vp/tlife_ip_attributes.cpp \
e_SportsSurcha_IP1_raw = 0 #-> Calc logiv in IL: /abs-rss-cpl/blob/main/ABS_MATHLIFE/src/math_life/vp/tlife_ip_surcharges.cpp \
e_sum_insured_raw = json.dumps(data['contract']['TVERTR_VORGABEN']['new'][0]['ABLAUFLEISTUNGSSUMME']) # Logic needed probably \
e_x_IP1_raw = json.dumps(data['contract']['TVERSPERS']['new'][0]['BEITRALTER']) \
e_x_IP2_raw = 0 # Second insured personis probably second item of TNATPERS \

e_pst_raw = json.dumps(data['contract']['TLSCHDETAIL']['new'][0]['GEWBETEILART']) \ 
e_StartDateYield_raw = 0  \
e_YieldDate_raw = 0 \
e_YieldValue_raw = 0 \

e_AddContrib_raw = 0 #-> Logic in IL \ 
e_AnnuityAmount_raw = 0 \
e_annutyPayFreq_raw = json.dumps(data['contract']['TPENSVEREINBG']['new'][0]['ZAHLWEISE']) \
e_BackOffice_raw = 0 \
e_CalcDate_raw = 0  \
e_CommReduction_raw = 0 \
e_currentDate_raw = 0 \
e_deathBenFactor_raw = 0 \ 
e_GrossPremium_raw = 0  \
e_j_raw = 0  \
e_InterestRate_raw = "Missing link to Tverstarif"#json.dumps(data['contract']['TVERSTARIF']['new'][0]['RECHZINS']) \ 
e_MainMaturity_raw = json.dumps(data['contract']['TVERTRAG']['new'][0]['HPTFLLG']) \
e_manual_LEBK_BWS_raw = 0  \
e_manual_LEBK_MON_raw = 0  \
e_manual_reserve_raw = 0  \
e_manualSumsOfPrem_raw = 0  \
e_method_raw = 0  \
e_PartSurrender_raw = 0 \ 
e_pfs_raw = 0  \
e_RateClass_raw = 0 \ 
e_SpecialDiscount_raw = 0 \ 
e_state_raw = 0  \
e_StateDetail_raw = 0 \ 
e_SumDiscount_raw = 0  \
e_SumOfPremiums_raw = 0  \
e_SumRelation_raw = 0  \
e_tarif_nr_raw = 0  \
e_tarsumme_gess_raw = 0 \ 
e_tarsumme_pfr_raw = 0  \
e_TBeg_raw = 0 \
e_wo_examination_raw = 0 \ 


### calculationbases - biometry

The biometry package involves two layers. 

1. The first layer determines the life table based on the tariff generation.
In case of several life tables for a single tariff generation the LifeTable class needs to reflect that logic.

2. The second layer calculates the probabilities based on the previously determined tables. 
So far the BiometryCpl class only yields probabilities for annuity tariffs.

### calculationbases - costs

The implementation of maxi formulas demands a clustered cost logic. For that purpose all tariffs were analysed and their
costs were clustered in the following way: https://docs.google.com/spreadsheets/d/1sIFjQ8Akmh2DNMp_mZu2motYrF-PQVRZ/edit#gid=484148070.

Four cost group families exist: "Acquisition Costs", "Amortization Costs", "Administration Costs" and 
"Unit Costs". Some cost groups have another layer of granularity, which depends on the deferment period or the contract 
status. The allocation of the cost group is done via the tariff name (e.g. "HA/2004") in CostMapping.py.

Each cost group has its own folder and the definition of the cost rate is always done with the same logic.
The cost rates can be accessed by "get_xyz_cost_by_name" function is used with the cost's name as a parameter.

### calculationbases - interest

The interest rate depends on the tariff generation and is returned as a vector. Future implementations which will 
calculate the Zinsratenzuschlag, that requires time-dependent interest rates can easily be implemented in that
framework

### calculationbases - flagsterms

Flags are a central element of the maxi formulas. The current implementation follows a two layered approach where (1) 
the formula to be used is based on the tariff name and (2) the flags are determined based on the formula. 

There are several flags used for the maxi formulas. 
1. mf_annuity_flags is used to determine the flags that are used to switch on functions in the maxi formula.
2. In cflags the present value terms are coded.
3. In eflags the cost terms are stored.

## Tests

Each package will be covered by a unit test. Those tests should assert the results of the function and also verify that 
all the functions are called with the correct arguments.

# Coding Guidelines (maryam heritage)
## IMPORTANT: General Guidelines
[General Clean Code Guidelines](https://cheatography.com/costemaxime/cheat-sheets/summary-of-clean-code-by-robert-c-martin/pdf/)
Summary of "Clean Code" by Robert C. Martin. __MUST READ__!

[General Guidelines](https://docs.python-guide.org/writing/style/)
The Hitchhiker's Guide to Python provides a great overview of how Python Code should look like!

## Type Hints
Python (>3.5) supports Type Hints. Type Hints help catching errors, helps documenting code, improves working with IDEs and linters and helps to build and maintain a cleaner architecture.
__Therefore new code should use type hints.__

[Documentation Type Hints](https://docs.python.org/3/library/typing.html)
## Classes
### Class Names
Class Names start with a capital letter. One Class per File (in general). Class Names should be a good description. 
[CamelCase](https://techterms.com/definition/camelcase) should be used for naming.

#### ATTENTION: Initialization of mutables (objects like lists, dicts, etc)
Proper initialization of mutables will reduce the risk of unexpected sideeffects. Mutables __should not__ be initialized at class level:
````python
class SomeClass:
    mutable = [] # DO NOT DO THIS
    def __init__(self):
        self.mutable.append(1) # SIDE EFFECT
````
The mutable would be shared among all instances of this class, because it will be instantiated at class and not on object-level, e.g. `self.mutable` will contain a `1`for __every initialization!__

Instead it should be approached like the following:
````python
class SomeClass:
    mutable: list[int] # DO THIS
    def __init__(self):
        self.mutable = []
        self.mutable.append(1)
````

#### Location & logic of Biometries
New biometries should be stored within `CPL_Testing/CalculationBases/Biometrie`. 

__OPEN:__ describe how new biometries can be added via LifeTable.py and CPL_BIO.py and their corresponding csv files. 

## Methods
### Naming
__WE DO NOT USE ABBREVIATIONS!__

(except if they are used mainly in the business domain, then we comment the meaning at initialization.)

Methods should always include a verb! 
For any type of calculation, the word ``compute`` is used. For every data returned, the word ``get`` is used.
__A method should either compute or return data! Not both!__

### Public / Private Methods
The less methods of a class are used from outside the class, the better. Every Method that is not intended to be used outside the class, should start with
double underscore: ``__get_private_something()``

### ATTENTION: Usage of mutables as default input parameters (objects like lists, dicts, etc)
Using mutables as default value can have unexpected side effects. Mutables __should not__ be used as default parameters:
````python
def do_something(mutable=[]): # DO NOT DO THIS
    mutable.append(1)
````
The mutable in the function signature would be shared among all calls of this method, if no value is provided, because the mutable will be instantiated once at runtime and not for every call, e.g. `mutable` will include a `1`for __every call!__

Instead it should be approached like the following:
````python
def do_something(mutable: list[int] = None): # DO THIS
    mutable = mutable if mutable is not None else list()
    mutable.append(1)
````
### Doc String
Every public method must include an appropriate DocString, which includes a description what the method does, the arguments it needs and what it returns.

[Reference - Multiline Docstrings](https://www.geeksforgeeks.org/python-docstrings/)
## Attributes
### Naming
__WE DO NOT USE ABBREVIATIONS!__

(except if they are used mainly in the business domain, then we comment the meaning at initialization.)

[CamelCase](https://techterms.com/definition/camelcase) should be used for naming.

### Public / Private Attributes
The less attributes accessible from outside of a class, the better. Every Attribute that is not intented to be used
outside of its class, should start with double underscore:
``__attributeName``
