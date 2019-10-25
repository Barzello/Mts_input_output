import argparse
import datetime
import time
import cv2
import csv

ap = argparse.ArgumentParser()
ap.add_argument("-o", "--output", type=str, default="output.csv",
	help="path to output CSV file containing point data")
args = vars(ap.parse_args())

def print_data():
    with open('inputs.csv') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        sk = list(reader)
        # for row in reader:
        print(sk[1][0])
        csvfile.close()
    with open('output.csv','w') as csvfile1:
        writer = csv.writer(csvfile1)
        writer.writerows(sk)
        csvfile1.close()
    with open('output.csv') as csvfile2:
        reader_out = csv.reader(csvfile2, delimiter=',')
        sk_out = list(reader_out)
        #START APPROXIMATION AND FILTRATION

        #END__
        print(sk_out)
        csvfile2.close()

# initialize the video stream and allow the camera sensor to warm up
print("[INFO] starting stream...")
print_data()

#while True:

   # if key == ord("q"):
   #     break

    # close the output CSV file do a bit of cleanup
#print("[INFO] cleaning up...")
#csv1.close()