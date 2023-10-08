import api from './api';

export async function registration(data) {
    const responce = await api.get('/api/v1/users/', {

    })
    return responce.data
}
