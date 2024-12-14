Test /register endpoint with a POST request:

{
    "username": "testuser",
    "password": "password123",
    "email": "testuser@example.com"
}

Test /login endpoint with a POST request:

{
    "username": "testuser",
    "password": "password123"
}


// posts and comments 

POST /api/posts/
{
    "title": "My First Post",
    "content": "This is the content of the post."
}

POST /api/comments/
{
    "post": 1,
    "content": "Great post!"
}
