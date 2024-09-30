ARG BUILD_FROM
FROM $BUILD_FROM

# Install required packages
RUN apk add --no-cache python3 py3-pip

# Copy data for add-on
COPY run.sh /
COPY meteo_lt_api.py /

# Install Python requirements
RUN pip3 install requests

# Execute during startup
CMD [ "/run.sh" ]
