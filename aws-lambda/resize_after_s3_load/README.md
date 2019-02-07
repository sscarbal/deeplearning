## 1. To create a deployment package for lambda from a python app

[Reference](https://docs.aws.amazon.com/lambda/latest/dg/with-s3-example-deployment-pkg.html#with-s3-example-deployment-pkg-python)

1. Create a directory with the app in it

2. Create a virtual environment in the app's directory
```
$ cd <app directory>

$ virtualenv --python=/usr/bin/python3.6 ./CreateThumbnail_venv

$ source ./shrink_venv/bin/activate
```
- Note: the configuration of the python version. The venv need to be one of the supported by aws-lambda. [Command from](https://stackoverflow.com/questions/1534210/use-different-python-version-with-virtualenv)

3. Install libraries in the virtual environment
```
$ pip install Pillow

$ pip install boto3
```

4. Add the contents of lib and lib64 site-packages to your .zip file.
```
$ cd $VIRTUAL_ENV/lib/python3.6/site-packages

$ zip -r <app base dir>/CreateThumbnail.zip .
```

5. Add your python code to the .zip file
```
$ cd <app directory>

$ zip -g CreateThumbnail.zip CreateThumbnail.py
```

## 2. To test the Lambda function

[Reference](https://docs.aws.amazon.com/lambda/latest/dg/with-s3-example.html#walkthrough-s3-events-adminuser-create-test-function-upload-zip-test-manual-invoke)

## 3. Upload the app to aws lambda

Upload the zip from with the app and the venv from the aws-lambda console. If the zip file is higher than 10 MB it is necesary upload it through S3.  
