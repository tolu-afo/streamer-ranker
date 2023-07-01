
import { Modal, modalStore } from '@skeletonlabs/skeleton';
import type { ModalSettings, ModalComponent } from '@skeletonlabs/skeleton';

export const customModal: ModalSettings = {
    type: 'prompt',
    title: 'Login',
    body: 'Provide your username and password in the fields below.',
    value: 'jsmith',
    valueAttr: { type: 'text', minlength: 3, maxlength: 10, required: true},
    response: (r: string) => alert("Alerting")
};
