try
    Step = Coord_Data(:,1);
    X = Coord_Data(:,2);
    Y = Coord_Data(:,3);

    X_MSD = MSD(X);
    Y_MSD = MSD(Y);

    Time = (Step+1)/20;
    Time(end) = [];
    
catch
    Coord_Data = [];
end



%% Functions

function out = MSD(X)
% Mean Square Displacement
    X_Square = repmat(X,1,length(X));

    X_Square_Diff = X_Square-X_Square.';
    X_Diff = tril(X_Square_Diff);
    X_Diff_Sqr = X_Diff.^2;
    
    X_Diff_Sqr_Col = spdiags(X_Diff_Sqr);
    X_Diff_Sqr_Col(X_Diff_Sqr_Col==0) = NaN;
    X_Diff_Sqr_Mn = nanmean(X_Diff_Sqr_Col);
    
    out = fliplr(X_Diff_Sqr_Mn);
end

    