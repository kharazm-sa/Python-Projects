
File_Extension = ".txt",".pdf",".gif",".png",".jpg",".jpeg",".zip"

def main():

    input_File = input ("Please enter the file path: ").strip().lower()
    if input_File.endswith(".txt"):
        print("text/plain")
    elif input_File.endswith(".pdf"):
        print("application/pdf")
    elif input_File.endswith(".gif"):
        print("image/gif")
    elif input_File.endswith(".png"):
        print("image/png")
    elif input_File.endswith(".jpg"):
        print("image/jpeg")
    elif input_File.endswith(".jpeg"):
        print("image/jpeg")
    elif input_File.endswith(".zip"):
        print("application/zip")
    else:
        print("application/octet-stream")
    
main()