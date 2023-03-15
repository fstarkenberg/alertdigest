FROM alpine:3.17

RUN \
  apk add --no-cache python3 curl && \
  python3 -m ensurepip && \
  if [ ! -e /usr/bin/pip ]; then ln -s pip3 /usr/bin/pip ; fi && \
  if [[ ! -e /usr/bin/python ]]; then ln -sf /usr/bin/python3 /usr/bin/python; fi && \
  pip install --upgrade pip && \
  adduser -D nonroot && \
  mkdir /app && \
  chown -R nonroot:nonroot /app

WORKDIR /app

# Copy files to system
COPY --chown=nonroot:nonroot . .

ENV VIRTUAL_ENV=/app/venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
WORKDIR /app
USER nonroot

RUN \
  python -m venv $VIRTUAL_ENV && \
  pip install --no-cache-dir -r requirements.txt

EXPOSE 9567
CMD ["gunicorn", "--bind=0.0.0.0:9567", "app:app"]
