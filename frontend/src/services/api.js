const API_BASE_URL = (
    import.meta.env.VITE_API_BASE_URL || "http://127.0.0.1:8000"
).replace(/\/$/, "");

const DEFAULT_TIMEOUT_MS = 15000;


async function request(path, options = {}) {
    const controller = new AbortController();
    const timeoutId = setTimeout(
        () => controller.abort(),
        DEFAULT_TIMEOUT_MS
    );

    try {
        const response = await fetch(
            `${API_BASE_URL}${path}`,
            {
                ...options,
                signal: controller.signal,
                headers: {
                    "Content-Type": "application/json",
                    ...(options.headers || {})
                }
            }
        );

        const payload = await response.json().catch(() => ({}));

        if (!response.ok) {
            const detail = payload.detail || `Request failed with status ${response.status}`;
            throw new Error(detail);
        }

        return payload;
    }
    catch (error) {
        if (error.name === "AbortError") {
            throw new Error("SupportIQ API request timed out. Check that the backend is running.");
        }
        throw error;
    }
    finally {
        clearTimeout(timeoutId);
    }
}


export function getHealth() {
    return request("/health", { method: "GET" });
}


export function getAnalytics() {
    return request("/analytics/", { method: "GET" });
}


export function getHistory() {
    return request("/analytics/history", { method: "GET" });
}


export function predictTicket(text) {
    return request(
        "/predict/",
        {
            method: "POST",
            body: JSON.stringify({ text })
        }
    );
}


// Backward-compatible alias used by the Analyzer page.
export function analyzeTicket(text) {
    return predictTicket(text);
}


// Backward-compatible alias used by dashboard components.
export function getPredictionHistory() {
    return getHistory();
}


export { API_BASE_URL };
