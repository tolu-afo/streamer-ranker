import { modalStore } from '@skeletonlabs/skeleton';

export const modal: ModalSettings = {
    type: 'prompt',
    title: 'Login',
    body: 'Provide your username and password in the fields below.',
    value: 'jsmith',
    valueAttry: { type: 'text', minlength: 3, maxlength: 10, required: true},
    response: (r: string) => alert('responsee:', r)
};

modalStore.trigger(modal);