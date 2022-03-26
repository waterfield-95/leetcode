def compute_avg_m(bias_correction=True):
    beta1 = 0.9
    G = 2
    t = 0
    m_t = 0
    m_sum = 0
    while t <= 100:
        t += 1
        m_prev = m_t
        m_t = beta1 * m_prev + (1 - beta1) * G
        if bias_correction:
            m_t_hat = m_t / (1 - pow(beta1, t))
        else:
            m_t_hat = m_t
        if t in [2, 10, 100]:
            m_sum += m_t_hat

    m_avg = m_sum / 3
    return m_avg

if __name__ == "__main__":
    q2_ans = compute_avg_m()
    q3_ans = compute_avg_m(False)
    print(q2_ans, q3_ans)