const API_URL = process.env.REACT_APP_API_URL;

export const analyzeInbox = (file) => {
  const form = new FormData();
  form.append("file", file);

  return fetch(`${API_URL}/inbox/analyze`, {
    method: "POST",
    body: form,
  }).then((res) => res.json());
};
