import Adapters.ConsolePrinter;
import Adapters.MovieReviewsRepo;
import Adapters.UserCommand;
import Application.MovieUser;
import Domain.MovieSearchRequest;
import Ports.IFetchMovieReviews;
import Ports.IPrintMovieReviews;
import Ports.IUserInput;

public class App {
    public static void main(String[] args) throws Exception {

        IFetchMovieReviews fetchMovieReviews = new MovieReviewsRepo();
        IPrintMovieReviews printMovieReviews = new ConsolePrinter();

        IUserInput userCommand = new UserCommand(fetchMovieReviews, printMovieReviews);

        MovieUser movieUser = new MovieUser(userCommand);
        
        MovieSearchRequest starWarsRequest = new MovieSearchRequest("StarWars");
        MovieSearchRequest starTrekRequest = new MovieSearchRequest("StarTrek");

        System.out.println("Displaying reviews for movie " + starTrekRequest.getMovieName());
        movieUser.processInput(starTrekRequest);

        System.out.println("Displaying reviews for movie " + starWarsRequest.getMovieName());
        movieUser.processInput(starWarsRequest);

    }
}
