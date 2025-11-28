resource "aws_instance" "sample" {
    ami = "ami-00d2efe5bc0683614"
    instance_type = "t2.micro"

    tags = {
        "Name" = "Sample"
    }
}

