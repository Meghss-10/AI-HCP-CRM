import axios from "axios";

const api = axios.create({
  baseURL: "https://ai-hcp-crm-an1i.onrender.com",
});

export default api;