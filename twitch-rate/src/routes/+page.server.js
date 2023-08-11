/** @type {import('./$types').Actions} */
export const actions = {
    // use actions to validate data, and post to server.
    login: async ({ cookies, request }) => {
        const data = await request.formData();

        console.log(data);
    },
    register: async ({ cookies, request }) => {
        const data = await request.formData();
        const p1 = data.get("password");
        const p2 = data.get("confirm_password");
        if (p1 == p2){
            console.log('passwords match')
            console.log('saving user....')
            const response = await fetch('http://localhost:8000/api/v1/users/', {
                method: 'POST',
                body: JSON.stringify({ 
                    'email': data.get('email'),
                    'username': data.get('username'),
                    'password': data.get('password')
                 }),
                headers: {
                    'Content-Type': 'application/json'
                }
            });
            console.log(response)
        }else {
            console.log("passwords don't match");
        }
        // console.log(data);

    }
    
};