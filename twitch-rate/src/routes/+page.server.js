/** @type {import('./$types').Actions} */
export const actions = {
    login: async ({ cookies, request }) => {
        const data = await request.formData();
        console.log(data);
    },
    register: async ({ cookies, request }) => {
        const data = await request.formData();
        console.log(data);
    }
    
};