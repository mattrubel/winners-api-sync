FROM public.ecr.aws/lambda/python:3.9

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt --target "${LAMBDA_TASK_ROOT}"

COPY lambda_app.py ${LAMBDA_TASK_ROOT}
COPY endpoints/. ${LAMBDA_TASK_ROOT}/endpoints/.
COPY interface/. ${LAMBDA_TASK_ROOT}/interface/.
COPY util/. ${LAMBDA_TASK_ROOT}/util/.

CMD [ "lambda_app.handler"]
