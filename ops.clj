(def operations [+ - / *])

(defn apply-random-operation [a b]
  (let [op (rand-nth operations)]
    (op a b)))

(apply-random-operation 2 3)

