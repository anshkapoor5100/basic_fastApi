# start your docker application
# run below commands to create image and run the container
docker build -t my-fastapi-app .      
docker run -p 8000:8000 my-fastapi-app

# open the below link for api docs
localhost:8000/docs