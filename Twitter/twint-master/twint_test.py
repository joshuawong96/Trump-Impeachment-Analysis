import twint
import time
import logging
import json

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                    datefmt='%m-%d %H:%M:%S')
                    # filename="crawl_log.txt",
                    # filemode="w")
logger = logging.getLogger(__name__)        

logging.getLogger('chardet.charsetprober').setLevel(logging.INFO)


# You will need to change output directory (OUTPUT_DIR), keyword, and  below configurations for your search 

# Configure
c = twint.Config()    
c.Store_CSV = True # store to json
# c.Media = True # only tweet with media
c.Retries_count = 10
c.Since = "2020-05-01 00:00:00"
c.Until = "2020-05-10 00:00:00"
c.Hide_output = True
c.Retweets = True
c.Debug = True
c.Stats = True    
# c.Limit = 10000

# If you want to collect tweets matching one keywords
keywords = 'phase3,singapore'
# # If you want to collect tweets matching any of multiple keywords (OR)
# keywords = '"vaccine" OR "blockchain"'
# # If you want to collect tweets containing all of those multiple keywords (AND)
# keywords = 'vaccine,blockchain'
logger.info("{}".format(keywords))
c.Search = keywords

OUTPUT_DIR = "./jsons"
filename = "vaccine_01"
c.Output = "{}/{}.jsons".format(OUTPUT_DIR, filename)

# Run
try:
    twint.run.Search(c)
except:
    logger.exception("error? sleeping 60 secs...")
    fe.write(keywords + "\n")
    time.sleep(60)

