FROM public.ecr.aws/lambda/python:3.8
COPY /ETL/app.py ./
CMD ["app.handler"]
