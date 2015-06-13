# readmeasurements 

A script to read and process sample hydrologic measurements.

## Usage
```
python readmeasurements.py DATAFILES
```

## Examples

Run one data file
```
$ python readmeasurements.py data/2012_measurements_sally.txt
data/2012_measurements_sally.txt

	temperature (celsius)
		 Average: 18.0833333333
		 Maximum: 30.0 occurred on 08/20/2012
		 Minimum: 4.0 occurred on 02/19/2012

	discharge (cfs)
		 Average: 100.333333333
		 Maximum: 110.0 occurred on 11/22/2012
		 Minimum: 91.0 occurred on 05/19/2012

	stage (ft)
		 Average: 12.1166666667
		 Maximum: 13.0 occurred on 11/22/2012
		 Minimum: 11.3 occurred on 07/21/2012
--------------------------------------------------
```

Run all data files
```
$ python readmeasurements.py data/*.txt
```

## Tests

Run test data file
```
$ python readmeasurements.py data/test_measurement_file.txt
data/test_measurement_file.txt

	temperature (celsius)
		 Average: 2.0
		 Maximum: 3.0 occurred on 01/01/2014
		 Minimum: 1.0 occurred on 02/01/2014

	precipitation (in)
		 Average: 0.15
		 Maximum: 0.2 occurred on 01/01/2014
		 Minimum: 0.1 occurred on 02/01/2014

	discharge (cfs)
		 Average: 15.0
		 Maximum: 20.0 occurred on 02/01/2014
		 Minimum: 10.0 occurred on 01/01/2014

	stage (ft)
		 Average: 1.5
		 Maximum: 2.0 occurred on 02/01/2014
		 Minimum: 1.0 occurred on 01/01/2014
--------------------------------------------------
```
