import axios from 'axios'

axios.defaults.baseUrl = "http://127.0.0.1:8000"

const instance = axios.create({})

export default instance;