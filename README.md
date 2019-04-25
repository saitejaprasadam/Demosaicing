# Demosaicing
Please adhere to your organization's rules for using this code. For [Concordia University](http://www.concordia.ca), these rules can be found [here](http://www.concordia.ca/students/academic-integrity/offences.html).

Part A

* Read Image
* Spilt into channels
* Applying filters to channel with appropiate kernel.
* Calculating difference
* Displaying image

Part B
* Performed all operations in part a till filter
* Converting to float32 to avoid under-over flow
* Computing G-R and B-R
* Applying median blur to GR and BR
* Computing G+R and B+R
* Converting back to unit8 (abs)
* Calculating difference
* Displaying images

As we are using kernel filters to interpolate the bayers pixel pattern (by taking some of the color percentage from neighbouring colors). This is the cause of artificats especially on the edges.
