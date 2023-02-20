# ChessVision
Deep Learning Class Project.  Created a dataset, built, trained, and tested a neural network to identify chess pieces.  

# Big Picture

This was a solo project, completed over a couple of very exciting weeks!  There were 3 main components:

* Creating a Dataset of Chess Images
 * After scouring the internet - I could not find a dataset of chesspiece images that would work for my project.  
 * I built several tools to help automate and streamline the process of reading chess files, speaking the required moves for a human to make on the board, then sync with my webcam to take the photos, and cut/crop/label the photo as necessary
* Building a small chess piecer classifier
 * It's a simple, but effective, CNN classifier.  
 * There were some interesting insights working on chess pieces, as disproportionate amount of the information about a pieces is encoded into the 'crown' of the piece.  Particularly Bishops/Queens/Kings can all look pretty similar from the neck down.  So the project report for more information on how I adapted to this problem

* Building and Testing an Object Detection program  
 * Using the classifier - I built a on Object Detection program to scan a (relatively sparse) chess board for object
 * The program slides a bounding box across images of the board, tracking boundaries that have confidently ID'd chess piece images.  The program then collapses overlapping boxes to get the most confident position of pieces


This was a wildly fun project to work on - and a great learning process!

See ProjectReport for more details