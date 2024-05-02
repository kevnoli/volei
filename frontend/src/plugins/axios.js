import axios from 'axios';

const instance = axios.create({
    baseURL: import.meta.env.VITE_API_URL,
    headers: {
        common: {
            "Accept": "application/json",
            "Content-Type": "application/json"
        }
    }
})

export default instance