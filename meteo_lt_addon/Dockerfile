ARG BUILD_FROM
FROM $BUILD_FROM

# Install required packages
RUN apk add --no-cache python3 py3-requests

# Copy data for add-on
COPY run.sh /
COPY meteo_lt_api.py /

# Make run.sh executable
RUN chmod a+x /run.sh

# Execute during startup
CMD [ "/run.sh" ]
