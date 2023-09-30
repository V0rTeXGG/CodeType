import api from './api';

export async function index() {
    const responce = await api.get('/users', {})
    return responce.data
}
