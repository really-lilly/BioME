# Software Design Components

## Input Data
This software requires the input data to be in .txt format. There are many bioinformatics platforms for pulling and consolidating bioinformatic data, any of which can be used prior to using this software. Most of these platforms will output files in OTU format, CSV, or .txt files. Some platforms bioinformatic platforms, such as QIIME (employed in the sample analysis), can output either OTU or .txt files and converting a .csv file into a .txt file will likely be trivial for BioME users.

## Component Specification

Component organization and interaction is relatively simple in BioME. With the exception of the data manager component, all components are feedforward and only need to interact with other components to feed data to other processes. There is no feedback or cross-talk between components. The data manager is the only component that communicates with the user and has a feedback loop to reprompt the data if it is incorrectly formatted.

1. ### Data manager
    * <ins> Function:</ins> Reads in OTU data and metadata and returns training and testing sets split randomly (90/10).
    * Input: A .txt file containing a biome data table and metadata containing keywords for disease or disease subtypes.
    * Output: Randomly split test and training sets as OTU tables.
    * Interactions: The user interacts with this component to enter data. This component prompts the user for data and re-prompts if the data entered is not correctly formatted. This component then interacts with the Data pre-processor by returning a correctly formatted input file to the data pre-processor. As this component has already ensured the data type is correct, there is no need for the data pre-processor to interact with the data manager other than simply accepting its output.
2. ### Data pre-processor
    * <ins> Function:</ins> Feature that standardizes the training and test OTU data. For some algorithms, this component uses a dimensionality reduction algorithm (optional) to condense the data into fewer features (particularly useful for microbiome data which inherently is very sparse).
    * Input: .txt formatted test and train datasets.
    * Output: Standardized (and condensed; optional) OTU formatted datasets for use in models.
    * Interactions: This component simply accepts data from the data manager. As the data manager ensures that data is formatted correctly, there is no need for the data pre-processor to communicate with the manager. This  interacts with the model fitting component by returning a cleaned and condensed dataset for the model fitting component to begin training. This component can also pass the same data to an optional feature analysis component.
3. ### Model fitting
    * <ins> Function:</ins> Read in OTU data and uses it to train a variety of machine learning models to most accurately fit the data.
    * Input: OTU formatted test and train datasets (can be condensed by the Data pre-processor component)
    * Interactions: This component can be considered a set of subcomponents executing machine learning algorithms in parallel (although for practical purposes, they may be executed one after another). Each subcomponent accepts a copy of the cleaned dataset from the data pre-processor and begins training a specific machine learning model. Each subcomponent passes its fitted model and a loss function value for the model. The subcomponents never interact with each other.
4. ### Model selector
    * <ins> Function:</ins> Evaluates the accuracy of each trained model (list specified by user) with the training set. Returns the model with the highest accuracy and allows the user to make a classification prediction on a new data point.
    * Input: Models trained by model fitting components, test set, list of models to test
    * Output: Trained models ordered by test accuracy, best-performing model that can be used to make a future prediction
    * Interactions: This component evaluates the accuracy of the models trained by the model fitting components and ranks them by accuracy score. It selects the most accurate model based on these values, and returns a list of the models tested and their respective accuracy scores and the best-performing model.


<p><img src="flowChart.PNG" height="650" width="1000" /></p>

# Interactions to accomplish use cases
The working mechanism of the specified components will be exemplified through the following use cases:
1. ### Medical clinician
    * **Goal:** Select the most accurate model to classify a disease or disease subtype using microbiome data from patients and utilize this model to predict a disease diagnosis using the selected model.
    * Without knowledge of popular machine learning algorithms, a medical clinician would simply need to input the OTU data gathered from patients with known disease diagnoses. The software is designed to function in an automated manner for this use case. The default is for the software to test all available ML algorithms and return an ordering of the trained models ordered by their predicted accuracies. With the most accurate model, the clinician will be able to input microbiome data for future patients and predict the disease subtype.
2. ### The microbiologist
    * **Goal:** Compare classification models of interest and analyze which bacteria are most strongly associated with a particular disease.
    * After sifting through the literature, the microbiologist will likely have a good idea of classification models that are popular in the microbiome community. They will have the option to specify which models they are interested in testing from a provided list of algorithms. This will provide them with a fast comparison of the selected models for their dataset. For those with strong datascience backgrounds, this software may also serve as a starting point for their classification model, allowing further customization for their dataset.
3. ### The ecologist
    * **Goal:** Select a classification model to utilize on data intended to better understand difference in features (bacteria) and diseases from samples in various environments.
    * This tool will serve as a screening to determine which algorithms classify their data most accurately. They can use this as a starting point to further develop an algorithm in R or another software that is more comfortable to them. Like in use case 1, the model produced can also be used directly to predict a label or disease classification for new samples that have been collected. The ecologist can then use these predictions to better understand environmental factors that may contribute to these diseases.



```python

```
