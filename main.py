import sys
import signal

# FILE = csvTSP250
NB_POPULATION = 200
NB_ITERATION = 1000
MAX_ITERATION = NB_ITERATION
DIFF_MAX = 4
FULL_DEBUG = True and False
RUNNING = True 

def getFormatedTime(t):
  d = int(t / (3600 * 24))
  res = t % (3600 * 24)
  h = int(res / 3600)
  res = res % 3600
  m = int (res / 60)
  res = res % 60

  response = ""
  if d:
    response += "{} d".format(d)
  if h:
    if response != "":
      response += ", "
    response += "{} h".format(h)
  if m:
    if response != "":
      response += ", "
    response += "{} m".format(m)
  if res:
    if response != "":
      response += ", "
    response += "{:.2f} s".format(res)

  return response

def stopRun(signal, frame):
  """
  Signal handler to stop infinite loop.
  @param    signal    The signal caucht.
  @param    frame     The frame.
  """
  global RUNNING
  RUNNING = False
  # exit(0)

if __name__ == '__main__':
  pass