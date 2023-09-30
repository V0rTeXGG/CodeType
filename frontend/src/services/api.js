import axios from 'axios'

axios.defaults.baseUrl = "http://127.0.0.1:8080"

const instance = axios.create({})

export default instance;