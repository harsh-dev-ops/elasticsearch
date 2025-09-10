docker cp elastic-stack-docker-part-two-es01-1:/usr/share/elasticsearch/config/certs/ca/ca.crt /tmp/.

openssl x509 -fingerprint -sha256 -noout -in /tmp/ca.crt | awk -F"=" {' print $2 '} | sed s/://g

cat /tmp/ca.crt > fleet-ca.yaml

# then add this 
# ssl:
    # certificate_authorities:
    # - |

# refer to this link: https://www.elastic.co/blog/getting-started-with-the-elastic-stack-and-docker-compose-part-2