// +-----------------------+
// |    Create Promise     |
// +-----------------------+
//            |
// +-----------+-----------+
// |                       |
// Pending               Fulfilled
// |                       |
// v                       v
// .then(onSuccess)       resolve(value)
// |                       |
// v                       v
// .catch(onError)      (Handle success)
// |                       |
// +-----------------------+
// |
// reject(error)
// |
// v
// Rejected (Error)
